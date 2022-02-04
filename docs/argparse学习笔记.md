# argparse 笔记

`argparse`这个包在很多项目中频繁使用，所以这里趁机尝试使用该包。

argparse是python用于解析命令行参数和选项的标准模块，其使用套路比较固定，这里复制一段代码作为演示：
```pyhton
import argparse

parser = argparse.ArgumentParser(description='test')

parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
parser.add_argument('--seed', type=int, default=72, help='Random seed.')
parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')

args = parser.parse_args()

print(args.sparse)
print(args.seed)
print(args.epochs)
```