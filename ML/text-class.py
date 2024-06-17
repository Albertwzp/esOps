from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# 初始化Elasticsearch客户端
es = Elasticsearch([{'host': '10.16.12.39', 'port': 9200, 'use_ssl': False}])

# 加载数据
data = es.search(index="sw_log", body={"query": {"match_all": {}}})
documents = [d["_source"]["content"] for d in data["hits"]["hits"]]
labels = [d["_source"]["service_id"] for d in data["hits"]["hits"]]

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.2, random_state=42)

print("start:")
print(len(X_train), len(X_test), len(y_train), len(y_test))
print(X_train[1], X_test[1], y_train[1], y_test[1])
print("end!")
# 构建随机森林分类器
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# 使用ES-ML库进行文本分类
from elasticsearch.ml.classification import ClassificationModel

model = ClassificationModel(clf.estimators_[0].feature_importances_, clf.estimators_[0].tree_.tree_)
model.fit(X_train, y_train)

# 预测新的文本
new_document = ["cms-api"]
prediction = model.predict(new_document)
print(prediction)
