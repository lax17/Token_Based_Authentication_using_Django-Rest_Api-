from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .constants import *
from .models import SignUpModel,AuthTokens
from .client_authentication import *
import base64


# Create your views here.





class Signup(APIView):
    authentication_classes = (ClientAuthentication,)
    def get(self, request):
        username = request.query_params.get("username")
        if not username:
            raise RequestBodyException(message="Please provide a username")
        try:
            client = SignUpModel.objects.get(username=username)
            ret = dict()
            ret["username"] = client.username
            ret["name"] = client.name
            ret["email"] = client.email
            ret["expiry_window"] = client.expiry_window
            with open(str(client.photo),"rb") as f:
                photo = base64.b64encode(f.read())
            ret["photo"] = photo
            return Response({"status": 200, "message": "done", "data": ret})
        except SignUpModel.DoesNotExist as e:
            return Response({"status": 200, "message": "Client not registered", "data": dict()})

    def post(self, request):
        try:
            request_data = request.data
            serializer = SignUpSerializer(data=request.data)
            if not serializer.is_valid():
                data = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            try:
                if SignUpModel.objects.get(email=request_data["email"]):
                    return Response({"status": 200, "message": request_data["email"] + " email id already exist", "data": dict()})
                if SignUpModel.objects.get(email=request_data["username"]):
                    return Response(
                    {"status": 200, "message": request_data["username"] + " username already exist", "data": dict()})
            except Exception as e:
                user = SignUpModel()
                user.name=request_data.get("name")
                user.username=request_data.get("username")
                user.email=request_data.get("email")
                user.set_password(request_data.get("password"))
                user.photo =request_data.get("photo")
                user.save()
            return Response(SIGNUP_SUCCESSFULLY_DONE)
        except Exception as e:
            return Response(str(e))

    def put(self, request):
        request_data = request.data
        serializer = EditProfileSerializer(data=request.data)
        if not serializer.is_valid():
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = SignUpModel.objects.get(username=request_data.get("username"))
            user.name = request_data.get("name")
            user.username = request_data.get("username")
            user.set_password(request_data.get("password"))
            user.photo = request_data.get("photo")
            user.save()
            return Response({"status": 200, "message": request_data.get("username") + " updated", "data": dict()})
        except SignUpModel.DoesNotExist as e:
            raise RequestBodyException(message="Client not registered.")

    def delete(self, request):
        username = request.data.get("username")
        if not username:
            raise RequestBodyException(message="Please provide a username.")
        try:
            client =SignUpModel.objects.get(username=username)
            client.is_deleted = True
            client.save()
            return Response({"status": 200, "message": username + " deleted", "data": dict()})
        except SignUpModel.DoesNotExist as e:
            raise RequestBodyException(message="username not registered.")


class Login(APIView):
    def post(self, request):
        request_data = request.data
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = SignUpModel.objects.get(username=request_data["username"])
            if not user.verify_password(request_data["password"]):
                return Response("Invalid Credentials")
            token = AuthTokens(user=user)
            token.save()
            return Response({"status": 200, "message": "token generated", "data": {"token": token.id}})
        except Exception as e:
            return Response({"Exception is {}".format(e)})



class Profile(APIView):
    authentication_classes = (ClientAuthentication,)
    def post(self,request):
        return Response({"status": "200"})








