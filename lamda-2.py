import json
# import sagemaker
import base64
import boto3
# from sagemaker.serializers import IdentitySerializer
runtime = boto3.client('runtime.sagemaker')


# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2022-01-13-02-53-08-312" ## TODO: fill in

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])## TODO: fill in

    # Instantiate a Predictor
    # predictor = sagemaker.predictor.Predictor(
    # ENDPOINT,
    # sagemaker_session=sagemaker.Session(), )## TODO: fill in

    # # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")

    # # Make a prediction:
    # inferences = predictor.predict(image) ## TODO: fill in

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image)
        
    inferences = response["Body"].read()
  
   
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    
    return {
        'statusCode': 200,
        'body': json.dumps(event["inferences"])
    }