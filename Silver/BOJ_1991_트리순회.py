

def pre_order(idx):
    global pre
    if idx >= 0 and idx <= 25:
        pre += tree[idx][1]
        pre_order(ord(tree[idx][0])-65)
        pre_order(ord(tree[idx][2])-65)

def in_order(idx):
    global ino
    if idx >= 0 and idx <= 25:
        in_order(ord(tree[idx][0])-65)
        ino += tree[idx][1]
        in_order(ord(tree[idx][2])-65)

def post_order(idx):
    global post
    if idx >= 0 and idx <= 25:
        post_order(ord(tree[idx][0])-65)
        post_order(ord(tree[idx][2])-65)
        post += tree[idx][1]

# 이진 트리
# A가 루트노드 / 알파벳26개
N = int(input())
tree = [[''] * 3 for _ in range(26)]            # 앞에서부터 A~Z로 채운다 0번 인덱스부터 시작
for _ in range(N):
    node = list(input().split())
    tree[ord(node[0])-65][0], tree[ord(node[0])-65][1], tree[ord(node[0])-65][2] = node[1], node[0], node[2]
pre = ''
ino = ''
post = ''
pre_order(0)
in_order(0)
post_order(0)
print(pre)
print(ino)
print(post)
