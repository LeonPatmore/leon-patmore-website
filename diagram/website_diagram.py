from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.mobile import APIGateway, Mobile
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.custom import Custom

font_colour = "black"

diagram_attributes = {
    "pad": "0.1",
    "fontsize": "50",
    "fontcolor": "white",
    "bgcolor": "transparent",
}

cluster_attributes = {
    "fontcolor": "black",
    "fontsize": "20"
}

with Diagram("Website Design",
             graph_attr=diagram_attributes,
             filename="my_website"):
    mobile = Mobile()
    with Cluster("CV", graph_attr=cluster_attributes):
        cv_store = S3()
    with Cluster("Images", graph_attr=cluster_attributes):
        image_store = S3()
    with Cluster("Lambda Function", graph_attr=cluster_attributes):
        fuc = LambdaFunction()
        nuxt = Custom(label="", icon_path="./nuxt.png")
        fuc >> Edge(style="dotted", color="darkgreen") >> nuxt
    with Cluster("API GW", graph_attr=cluster_attributes):
        api_gw = APIGateway()
    api_gw >> Edge(color="black") >> fuc
    with Cluster("leonpatmore.com", graph_attr=cluster_attributes):
        r53 = Route53()
    mobile >> Edge(color="black") >> r53 >> Edge(color="black") >> api_gw
    cv_store << Edge(color="black") << mobile
    image_store << Edge(color="black") << mobile
