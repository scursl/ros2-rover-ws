#!/bin/bash

message = $1

git add .
git status
git commit -m $message
git push origin main