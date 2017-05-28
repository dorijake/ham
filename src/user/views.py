from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Friends
from django.db.models import Q

# Create your views here.

@login_required
def friend_list(request):
	user_id = request.user.id

	friend_list = Friends.objects.filter(user_id=user_id).prefetch_related('user')
	for f in friend_list:
		print(f.friend_id)
	return render(request, 'user/friend_list.html', {'friend_list':friend_list,})