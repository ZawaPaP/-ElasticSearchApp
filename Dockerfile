FROM docker.elastic.co/elasticsearch/elasticsearch:7.17.23
RUN elasticsearch-plugin install analysis-kuromoji