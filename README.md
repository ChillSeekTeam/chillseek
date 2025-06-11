# chillseek
Machine learning to identify mechanical equipment on aerial images

# PROJECT WORKFLOW #
+ Develop locally on devcontainer
+ When fulsome compute required, connect to Azure ML instance

#TO DO#

+ Get initial set of projects from TRAX deliverables
+ use address to get images from TRAX deliverables
+ need to convert address to geojson
+ use zero-shot to identify the buildings in the images ....... this will get you better image quality?
+ how to toggle between CPU and GPU VMs???
    + i just need to be clear about pipeline splits;
    + so files / notebooks where GPU compute is done and separate ones for CPU
+ build front-end to show the address, images, and deliverables
+ build back-end to serve up the images (should I do it in fastapi, django, or javascript?)


END STATE GOAL (when complete)
+ given an address
+ get image of the address; zero-shot to find images of the building
+ use Roboflow model for inference to analyze HVAC equipment
+ find old image of the building ????
+ compare old image to new image ... how different?
+ score the building for opportunity
+ website to show buildings ranked by potential opportunity

TO GET THERE
+ get current images
+ where can we get OLD images and how much would it cost?