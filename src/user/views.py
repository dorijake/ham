from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Friends, Friends_Status
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
import json
from .forms import FriendsForm, UserProfileForm
from django.forms.models import model_to_dict
from django.contrib.auth.forms import AuthenticationForm
from home.forms import UserCreationForm
from django.urls import reverse


# Create your views here.

@login_required
def friend_list(request):
	current_user_id = request.user.id
	

	friend_list = User.objects.get_friends(id=current_user_id)
	
	
	return render(request, 'user/friend_list.html', {'friend_list':friend_list,})


@login_required
def search_user(request):

	USER_RELELATION = {'MYSELF':1, 'FRIEND':2, 'NO_RELATION':3,}

	username = request.POST.get('keyword')
	user_list = User.objects.filter(username__contains=username).values('id', 'username',)

	current_user_id = request.user.id
	friends = User.objects.get_friends(id=current_user_id)
	friend_list = [friend['friend_id'] for friend in friends]

	for user_searched in user_list:
		status = 0
		
		if user_searched['id'] == current_user_id:
			status = USER_RELELATION['MYSELF']

		elif user_searched['id'] in friend_list:
			status = USER_RELELATION['FRIEND']

		else:
			status = USER_RELELATION['NO_RELATION']

		user_searched['relation'] = status

	
	return HttpResponse(json.dumps({'user_list':list(user_list),}), content_type='application/json')


@login_required
@csrf_protect
def add_friend(request):

	user1_id = int(request.POST.get('user1_id'))
	user2_id = int(request.POST.get('user2_id'))
	action_user_id = int(request.POST.get('action_user'))
	status_id = Friends_Status.objects.get(name='requesting').code

	form_data = {
		'user1':user1_id,
		'user2':user2_id,
		'action_user':action_user_id,
		'status':status_id
	}

	friends_form = FriendsForm(data=form_data)
	
	if request.method == "POST":
		if friends_form.is_valid():
			obj = friends_form.save()
			
			return HttpResponse(json.dumps({'friends':model_to_dict(obj)}), content_type='application/json')

	return HttpResponse()



def delete_friend(request):

	current_user_id = request.user.id
	friend_id = int(request.POST.get('friend_id'))

	friend_list = User.objects.get_friends(current_user_id)
	friend_id_list = [friend_id['friend_id'] for friend_id in friend_list]

	friend = Friends.objects.filter(Q(user1=current_user_id, user2=friend_id) | Q(user1=friend_id, user2=current_user_id))

	response = {}

	if request.method == "POST":

		if friend:
			friend.delete()
			response['result'] = 'success'
		else:
			response['result'] = 'failed'


	
	return HttpResponse(json.dumps(response), content_type='application/json')


@login_required
def mypage(request):
	redirect_to = reverse('profile')

	return HttpResponseRedirect(redirect_to)


@login_required
def password_confirm(request):

	if request.method == "POST":
		
		username = request.POST.get('username')
		password = request.POST.get('password')

		data = {'username':username, 'password':password}

		form = AuthenticationForm(data=data)
		
		response = {}

		if form.is_valid():

			redirect_to = request.POST.get('next')

			response['result'] = 'success'
			response['next'] = redirect_to


		else:
			response['result'] = 'failed'
			response['msg'] = 'invalid password'


		return HttpResponse(json.dumps(response), content_type='application/json')


	next = request.GET.get('next')

	return render(request, 'user/password_confirm.html', {'next':next})


@login_required
def profile(request):
	userid = request.user.id

	user = User.objects.get(id=userid)

	return render(request, 'user/profile.html', {'user':user})


@login_required
def edit_profile(request):

	if request.method == "POST":
		userid = request.user.id
		user = User.objects.get(pk=userid)

		form = UserProfileForm(request.POST, instance=user)

		if form.is_valid():

			form.save()

			return HttpResponseRedirect(reverse('profile'))

	else:

		form = UserProfileForm()

	return render(request, 'user/edit_profile.html', { 'form':form })

