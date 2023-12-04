#!/bin/bash

# ngrok 실행을 위한 포트
LOCAL_PORT=5000

# ngrok 실행
ngrok http $LOCAL_PORT
