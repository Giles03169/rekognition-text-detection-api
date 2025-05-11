# AWS Rekognition Text Detection API

## 🧠 Description
This project demonstrates how to build a serverless API using AWS Lambda, API Gateway, and Rekognition to detect printed text in images. Images are sent as base64-encoded strings, processed by Rekognition, and the detected text lines are returned.

## 🧰 Tech Stack
- AWS Lambda (Python 3.12)
- Amazon Rekognition (DetectText)
- API Gateway (HTTP API)
- Base64 Image Encoding
- HTML + JS Frontend (Optional)

## 🚀 Setup Instructions
1. Create an IAM Role with `rekognition:DetectText` permission.
2. Create a Lambda function and paste the code from `lambda_function.py`.
3. Deploy an HTTP API in API Gateway with a POST route `/ocr` integrated to your Lambda.
4. Enable CORS and deploy to a stage (e.g., `dev`).
5. Test with a base64-encoded image via Postman or a basic HTML form.

## 📁 Folder Structure
