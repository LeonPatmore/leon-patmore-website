from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.mobile import APIGateway, Mobile
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.custom import Custom

font_colour = "black"

diagram_attributes = {
    "pad": "0.1",
    "fontsize": "45",
    "fontcolor": font_colour,
    "bgcolor": "transparent",
}

with Diagram("Website Design",
             graph_attr=diagram_attributes,
             node_attr={"fontsize": "18", "fontcolor": font_colour},
             filename="my_website"):
    mobile = Mobile()
    with Cluster("CV"):
        cv_store = S3()
    with Cluster("Images"):
        image_store = S3()
    with Cluster("Lambda Function"):
        fuc = LambdaFunction()
        nuxt = Custom(label="Nuxt", icon_path="./nuxt.png")
        fuc >> Edge(style="dotted", color="darkgreen") >> nuxt
    with Cluster("API GW"):
        api_gw = APIGateway()
    api_gw >> Edge(color="black") >> fuc
    with Cluster("leonpatmore.com"):
        r53 = Route53()
    mobile >> Edge(color="black") >> r53 >> Edge(color="black") >> api_gw
    cv_store << Edge(color="black") << mobile
    image_store << Edge(color="black") << mobile
