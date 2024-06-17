from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# 初始化Elasticsearch客户端
es = Elasticsearch([{'host': '10.16.12.39', 'port': 9200, 'use_ssl': False}])

# 加载数据
data = es.search(index="sw_log", body={"query": {"match_all": {}}})
documents = [d["_source"]["content"] for d in data["hits"]["hits"]]
labels = [d["_source"]["service_id"] for d in data["hits"]["hits"]]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# 加载标签编码器
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# 使用K-means进行文本聚类
kmeans = KMeans(n_clusters=10)
kmeans.fit(X)

# 预测新的文本
new_document = ["mda-dev00-http"]
new_X = vectorizer.transform(new_document)
prediction = kmeans.predict(new_X)
print(prediction)
