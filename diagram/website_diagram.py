from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.mobile import APIGateway, Mobile
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.custom import Custom

diagram_attributes = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

cluster_attributes = {
    "bgcolor": "transparent",
}

with Diagram("My Website", graph_attr=diagram_attributes):
    mobile = Mobile("User")
    cv_store = S3("CV")
    image_store = S3("Images")
    with Cluster("Lambda Function", graph_attr=cluster_attributes):
        fuc = LambdaFunction()
        nuxt = Custom(label="Nuxt", icon_path="./nuxt.png")
        fuc >> Edge(style="dotted", color="darkgreen") >> nuxt
    api_gw = APIGateway("Api GW")
    api_gw >> fuc
    mobile >> Route53("leonpatmore.com") >> api_gw
    cv_store << mobile
    image_store << mobile
