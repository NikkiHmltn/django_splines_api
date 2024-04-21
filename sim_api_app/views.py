from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import SimsPack, Trait
from .serializers import *

import requests

# Create your views here.
@api_view(['GET'])
def get_all_packs(request):
    try:
        all_packs = SimsPack.objects.all()
        serializer = SimsPackSerializer(all_packs, context={'request', request}, many=True)
        return Response(serializer.data)
        if len(serializer.data) <= 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except SimsPack.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_traits(request):
    try:
        all_traits = Trait.objects.all()
        serializer = TraitSerializer(all_traits, context={'request', request}, many=True)
        return Response(serializer.data)
        if len(serializer.data) <= 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Trait.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def filter_lot_traits_by_pack(request, pack_pk):
    try:
        pack_traits = Trait.objects.filter(Q(type='LC') | Q(type='LT'), pack=pack_pk)
        serializer = TraitSerializer(pack_traits, context={'request', request}, many=True)
        if len(serializer.data) <= 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    except Trait.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filter_sim_traits_by_pack(request, pack_pk):
    try: 
        sim_traits = Trait.objects.filter(pack=pack_pk, type="ST")
        serializer = TraitSerializer(sim_traits, context={'request', request}, many=True)
        if len(serializer.data) <= 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    except Trait.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def filter_ambition_by_pack(request, pack_pk):
    try:
        ambitions = Trait.objects.filter(pack=pack_pk, type='AM')
        serializer = TraitSerializer(ambitions, context={'request', request}, many=True)
        if len(serializer.data) <= 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    except Trait.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filter_sim_skills_by_pack(request, pack_pk):
    try:
        skills = Trait.objects.filter(pack=pack_pk, type="SK")
        serializer = TraitSerializer(skills, context={'request', request}, many=True)
        if len(serializer.data) <= 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    except Trait.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)