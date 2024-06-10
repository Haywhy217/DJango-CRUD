from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def get_users(request):
    if request.method == "GET":
       user = user.objects.all()
    return JsonResponse({
        'status': 'success',
        'user': list(user.values())
    }), 200

@csrf_exempt
def add_user(request):
  if request.method =="POST":
      json_data = request.body .decode("utf-8")
      data_dict = json.loads(json_data)
      user= data_dict.get("first_name")
      existing_user = user.objects(first_name = user)
      if existing_user:
        return JsonResponse({"message": "user with this name already"},status = 400 )
      else:
        user.objects.create(
           first_name = "Ayomide",
            last_name = "Olanipekun",                 
            image_url =" image.png")
        return JsonResponse({
      "message": "post added successfully" })
  else: 
   return JsonResponse({"message": "invalid method"},status=405)

@csrf_exempt
def edit_user(request):
    if request.method =="PUT":
        json_data = request.body .decode("utf-8")
        data_dict = json.loads(json_data)
        user_id = data_dict.get("user_id")
        if user_id:
            try:
                      user = user.objects.get(id=user_id)
            except user.DoesNotExist: 
                  return JsonResponse({"message": "user not found"}, status=404)
              
            if "first_name" in data_dict:
                    user.name = data_dict["first_name"]
            if "last_name" in data_dict:
                    user.name = data_dict["last_name"]
            if "image" in data_dict:
                      user.image_url = data_dict["image"] 
                      user.save()

        return JsonResponse({"message": "user updated successfully"}, status=200)
    else:
        return JsonResponse({"message":"invalid method"}, status=405)
            

@csrf_exempt
def delete_user(request):
    if request.method == "DELETE":
        json_data = request.body .decode("utf-8")
        data_dict = json.loads(json_data)
        user_id = data_dict.get("user_id")
        try:
            user = user.objects.get(id=user_id)
            user.delete()
            return JsonResponse({}, status=204) 
        except user.DoesNotExist:
            return JsonResponse({"message": "user not found"}, status=404)
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)

