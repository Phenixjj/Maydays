#!/bin/bash

# Change to your project directory
cd /Users/jeanlecigne/IdeaProjects/Maydays/maydays

# Install dependencies
npm install

# Build your project
npm run build

# Deploy using Firebase
firebase deploy