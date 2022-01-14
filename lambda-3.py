import json



THRESHOLD = .93


def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = json.loads(event["body"])
    inferences = inferences.replace(']', '')
    inferences = inferences.replace('[', '')
    inferences = inferences.replace(',', '')
    inferences = list(inferences.split(" "))
    
    print (inferences)
    ## TODO: fill in
    
    def check(inferences):
        for i in inferences:
            print (i)
            if float(i) > THRESHOLD:
                return True

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = check(inferences) ## TODO: fill in

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }