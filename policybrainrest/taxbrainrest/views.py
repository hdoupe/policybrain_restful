from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from taxbrainrest.models import ModelMeta, ModelInput, ModelResult
from taxbrainrest.serializers import ModelInputSerializer, ModelResultSerializer


class TaxBrainStaticModelInputList(APIView):

    def get(self, request, format=None):
        model_inputs = ModelInput.objects.all()
        serializer = ModelInputSerializer(model_inputs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ModelInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxBrainStaticModelInputDetail(APIView):

    def get_object(self, pk):
        try:
            ModelInput.objects.get(pk=pk)
        except ModelInput.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        model_input = self.get_object(pk)
        serializer = ModelInputSerializer(model_input)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        raise Http404 # not implemented

    def delete(self, request, pk, format=None):
        raise Http404 # not implemented
