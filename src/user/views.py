from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Friends
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
import json

# Create your views here.

@login_required
def friend_list(request):
	current_user_id = request.user.id
	
	friend_list = User.objects.get_friends(id=current_user_id)
	
	
	return render(request, 'user/friend_list.html', {'friend_list':friend_list,})


@login_required
@csrf_protect
def search_user(request):

	USER_RELELATION = {'MYSELF':1, 'FRIEND':2, 'NO_RELATION':3,}

	username = request.POST.get('username')
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

	FRIEND_STATUS = ''
	user_id = request.POST.get('user_id')
	friend_id = request.POST.get('friend_id')
	

	
