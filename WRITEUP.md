# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*

#### **1. costs**  
|VM|App Service|
|-----------|------------|
|cost may varies, depends on options |provides free tier for a year|  
| B1S machines will costs $0.0104/hour, $60.51/month | Basic, B1 will costs $73.65/month|


#### **2. Scalability**
|VM|App Service
|-----------|------------|
| VM scale sets| Built in service|
|Azure Load Balancer| Integrated | 
|Platform images: 1000 nodes per scale set, Custom images: 600 per nodes per scale set| 20 instances, 100 with App Service Environment|

#### **3. availability**
|VM|App Service
|-----------|------------|
|Broad range of VM SLAs: from single-instance at 99.9%| Achieve high availability with SLA-backed uptime of 99.95%
|Traffic manager | Traffic manager|


#### **4. workflow**
|VM|App Service
|-----------|------------|
| Create VM | Create WebService|
| Create SSH connection with the VM | Deploy Web App from Github |
| Install Web Server|
| Deploy Web Application | 
|Use public IP address to view web| Navigate to the deployed URL| 


#### **AppService deployment solutions:**
1. Create "Web App" on the azure portal
2. Setting configurations:
    + resource-group
    + web app name
    + publish: Code
    + Runtime stack: python 3.7
    + Operating System: Linux
    + Region
    + App Service Plan
    + SKU and size: F1 (free tier)
3. Deploy the App Service Web App
    + deploy the Web app from GitHub on Azure portal>Deployment Center
4. Navigate to the deployed URL

#### **I CHOSE AppService** since CMS App is lightweight and won't approach to the size limit for App Services easily. Moreover, easy to deploy from the Azure Portal which requries much faster deployments.


### Assess app changes that would change your decision.
#### App Service:
If CMS Appliction requires more complex functions and needs more 


##### **Reference:
##### https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree