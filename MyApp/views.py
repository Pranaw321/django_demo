from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from rest_framework.views import APIView


