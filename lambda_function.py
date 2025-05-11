import boto3
import json
import base64

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    try:
        print("Event Received:", json.dumps(event))
        
        body = json.loads(event['body'])
        image_data = base64.b64decode(body['image'])

        response = rekognition.detect_text(
            Image={'Bytes': image_data}
        )

        detected_text = []
        for item in response['TextDetections']:
            if item['Type'] == 'LINE':
                detected_text.append({
                    'DetectedText': item['DetectedText'],
                    'Confidence': item['Confidence']
                })

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({'text': detected_text})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
