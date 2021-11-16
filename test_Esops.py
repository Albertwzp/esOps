import sys
sys.path.append("./")
import esOps

if __name__ == '__main__':
    ops = esOps.Es.connect(host="172.25.49.2", port=9200)
    ops.ping()
    ops.info()
