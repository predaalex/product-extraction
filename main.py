import sparknlp
# make sure the next command doesn't have any error or failed downloads
# this is where the JAR and the dependencies are being downloaded
# so if you are behind the firewall, or proxy or lose internet connectivity it won't load it
# and you see that error
spark = sparknlp.start()

print(spark.version)

sparknlp.version()
