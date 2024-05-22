# K8S GPT Discovery

K8sGPT is a tool for scanning your kubernetes clusters, diagnosing and triaging issues in simple english. It has SRE experience codified into it’s analyzers and helps to pull out the most relevant information to enrich it with AI.

## Installation

### For MacOS/Linux users

```bash
brew tap k8sgpt-ai/k8sgpt
brew install k8sgpt
brew install kind
```

List the commands available
```bash
k8sgpt --help
```

## Remote Setup

Add your openAI api key
```bash
k8sgpt auth list
k8sgpt auth add openai
```

## Local Setup

Git clone LoacalAI repository
```bash
git clone https://github.com/go-skynet/LocalAI
cd LocalAI
```

Download models from gpt4ll
```bash
wget https://gpt4all.io/models/ggml-gpt4all-j.bin -O models/ggml-gpt4all-j
```
Copy prompts to models folder
```bash
cp -rf prompt-templates/ggml-gpt4all-j.tmpl models/
```

Run LocalAI using Docker-compose
```bash
docker-compose up -d --pull always
```

Verify API running
```bash
curl http://localhost:8080/v1/models
```
```bash
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json" -d '{
     "model": "ggml-gpt4all-j",
     "messages": [{"role": "user", "content": "How are you?"}],
     "temperature": 0.9
   }'
```
Survey logs
```bash
docker logs -f localai-api-1
```

**A few moment (with CPU) later...got an answer**

```json
{
    "created":1716370961,
    "object":"chat.completion",
    "id":"0200c4c1-b77c-4551-973c-40875094ac52",
    "model":"ggml-gpt4all-j",
    "choices":[{
        "index":0,
        "finish_reason": "stop",
        "message":{
            "role":"assistant",
            "content":"I'm doing well. How about you?"
        }
    }],
    "usage":{
        "prompt_tokens":0,
        "completion_tokens":0,
        "total_tokens":0
    }
}
```

Add localai to k8sgpt

```bash
k8sgpt auth add --backend localai --model ggml-gpt4all-j --baseurl http://localhost:8080/v1
```

Create a deployement with ErrImagePull for testing

```bash
touch deployment.yaml
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: ngisduycvsudycnx:1.14.2 # error in the image name
        ports:
        - containerPort: 80
```

Deploy Nginx server
```bash
kubectl apply -f deployment.yaml
kubectl get pods --all-namespaces
```

Ask K8SGPT what's going wrong

```bash
k8sgpt analyse --explain --backend localai
```

K8SGPT answer : 
```
100% |█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| (2/2, 1 it/min)           
AI Provider: localai

0: Pod default/nginx-6bddbdd98f-j78vh(Deployment/nginx)
- Error: failed to pull and unpack image "docker.io/library/ngisduycvsudycnx:1.14.2": failed to resolve reference "docker.io/library/ngisduycvsudycnx:1.14.2": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
The error message indicates that the repository "docker.io/library/ngisduycvsudycnx:1.14.2" does not exist or may require authorization, but the user does not have sufficient scope to access it. 
To resolve this issue, the user can try to:
1. Check if the repository exists by running `docker search ngisduycvsudycnx`
2. If the repository does not exist, create it by running `docker login` and then run the command to pull it.
3. If authorization is required, the user can try to add their Docker credentials by running `docker login` and then run the command to pull it.
4. If none of the above solutions work, try to contact Docker support for further assistance.
1: Pod default/nginx-6bddbdd98f-mck88(Deployment/nginx)
- Error: failed to pull and unpack image "docker.io/library/ngisduycvsudycnx:1.14.2": failed to resolve reference "docker.io/library/ngisduycvsudycnx:1.14.2": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
The error message indicates that the repository "docker.io/library/ngisduycvsudycnx:1.14.2" does not exist or may require authorization, but the user does not have sufficient scope to access it. 
To resolve this issue, the user can try to:
1. Check if the repository exists by running `docker search ngisduycvsudycnx`
2. If the repository does not exist, create it by running `docker login` and then run the command to pull it.
3. If authorization is required, the user can try to add their Docker credentials by running `docker login` and then run the command to pull it.
4. If none of the above solutions work, try to contact Docker support for further assistance.
```

## Tools
* Kubernetes
* Kind
* OpenAI API
* LocalAI
* K8SGPT
* GPT4ALL
* Docker
* Docker-compose
* k9s

## Contributing
Contributions to the project are welcome! To contribute:

* Fork the repository
* Create a new branch (`git checkout -b feature/my-feature`)
* Commit your changes (`git commit -am 'Add a new feature'`)
* Push the branch (`git push origin feature/my-feature`)
* Open a Pull Request

## Author
Jean LECIGNE

