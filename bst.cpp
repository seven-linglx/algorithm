//
// Created by linglx on 18-8-9.
//

#include <iostream>
#include <sstream>
#include <vector>
#include <queue>

typedef struct BinaryTree
{
  BinaryTree()
  {
    value = 0;
    left = nullptr;
    right = nullptr;
  };

  int value;
  BinaryTree* left;
  BinaryTree* right;
} Node;

template <typename T>
inline std::ostream& operator<<(std::ostream& o, std::vector<T> const& v)
{
  std::stringstream s;
  for (int i = 0; i < v.size(); i++)
  {
    if (i != v.size() - 1)
      s << v[i] << ", ";
    else
      s << v[i];
  }
  return o << s.str();
}

void createBinaryTree(Node*& node, const int& value)
{
  if (node == nullptr)
  {
    node = new Node();
    node->value = value;
    return;
  }

  if (node->value > value)
    createBinaryTree(node->left, value);
  else
    createBinaryTree(node->right, value);
}

void printPreorder(Node* const& node)
{
  if (node == nullptr)
    return;
  else
    std::cout << node->value << ", ";
  printPreorder(node->left);
  printPreorder(node->right);
}

void printLevelOrder(Node* const& root)
{
  std::vector<int> level_data;
  std::queue<Node*> node_queue;
  node_queue.push(root);
  node_queue.push(nullptr);
  while (!node_queue.empty())
  {
    Node* front = node_queue.front();
    node_queue.pop();
    if (front != nullptr)
    {
      level_data.push_back(front->value);
      if (front->left != nullptr)
        node_queue.push(front->left);
      if (front->right != nullptr)
        node_queue.push(front->right);
    }
    else if (!node_queue.empty())
    {
      node_queue.push(nullptr);
      std::cout << level_data << std::endl;
      level_data.clear();
    }
  }
}

int main(int argc, char* argv[])
{
  int a[5] = { 8, 2, 3, 9, 7 };
  BinaryTree* root = new BinaryTree();
  root->value = 5;
  for (const auto& i : a)
  {
    createBinaryTree(root, i);
  }
  printPreorder(root);
  std::cout << std::endl;
  printLevelOrder(root);
  return 0;
}
