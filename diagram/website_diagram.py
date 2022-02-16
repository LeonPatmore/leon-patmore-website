from diagrams import Diagram
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.mobile import APIGateway
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3

with Diagram("Website"):
  cv_store = S3("CV")
  image_store = S3("Images")
  fuc =  LambdaFunction("Nuxt Function")
  fuc >> cv_store
  fuc >> image_store
  Route53("dns") >>  APIGateway("Api GW") >> fuc
