# ML App on EC2 with Docker (GitHub + CodePipeline + CodeDeploy)

Iris flower prediction (scikit-learn + Flask) running inside a Docker container on EC2.

## Push to GitHub
    git init
    git add .
    git commit -m "ML docker app v1"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/ec2-docker-deployment.git
    git push -u origin main

appspec.yml must stay in the repo root and scripts/ must contain both .sh files.

## Check on EC2 (PuTTY)
    sudo docker ps
    sudo docker logs ml-app
    curl http://localhost
