from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from model_api.models import UploadImageTest
from .serializers import ImageSerializer
from rest_framework import permissions
from django.templatetags.static import static
import numpy as np
from PIL import Image
import requests
from django.http import HttpResponse, JsonResponse
import json
from django.core.files.storage import default_storage



class TodoListApiView(APIView):
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        todos = UploadImageTest.objects.all()
        serializer = ImageSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # data = {
        #     'image': request.data.get('image'), 
        # }
        def load_image_into_numpy_array(path):
            return np.array(Image.open(path))

        # path = './static/003.jpeg'
        file = request.data['image']
        image = UploadImageTest.objects.create(image=file,name=request.data['name'])
        # return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

        # path = './003.jpeg'
        path = './media/images/'+file.name
        # PATH = 'https://storage.googleapis.com/ecocrafters_bucket/000001.jpg'

        test_image = load_image_into_numpy_array(path)
        reshaped_image = np.expand_dims(test_image, 0)
        data = json.dumps({"signature_name": "serving_default", "instances": reshaped_image.tolist()})
        headers = {"content-type": "application/json"}
        # json_response = requests.post('http://localhost:8501/v1/models/my_ssd_mobnet:predict', data=data, headers=headers)
        json_response = requests.post('https://model-check-iftqmea47q-et.a.run.app/v1/models/my_ssd_mobnet:predict', data=data, headers=headers)
        predictions = json.loads(json_response.text)['predictions']
        # with open('result.json', 'w') as f:
        #     json.dump(json_response.json(), f, indent=4)
            
        boxes = predictions[0]['detection_boxes']
        scores = predictions[0]['detection_scores']
        labels = predictions[0]['detection_classes']


        # Visualize the results
        # image = test_image

        # Create figure and axes
        # fig, ax = plt.subplots(1)
        # ax.imshow(image)

        # Iterate over the bounding boxes and plot them
        label_final = []
        for box, score, label in zip(boxes, scores, labels):
            ymin, xmin, ymax, xmax = box

            if score < 0.3:
                continue
            # width, height = image.shape[1], image.shape[0]
            # left = xmin * width
            # right = xmax * width
            # top = ymin * height
            # bottom = ymax * height
            # rect = patches.Rectangle((left, top), right - left, bottom - top, linewidth=1, edgecolor='r', facecolor='none')
            # ax.add_patch(rect)
            # label_text = f'Class: {label}, Score: {score:.2f}'
            # ax.text(left, top - 5, label_text, color='r')
            label_final.append(label)

        # Show the image with bounding boxes and labels
        # print(label_final)
        # return HttpResponse(label_final)
        # serializer = ImageSerializer(label_final, many=False)
        print(type(label_final))
        return Response(label_final,status=status.HTTP_200_OK)
        # return JsonResponse(json.dumps(label_final))

        # serializer = ImageSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)