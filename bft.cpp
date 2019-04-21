//
// Created by Administrator on 2018/4/5 0005.
//

#include <iostream>

using namespace std;

struct TreeNode;
typedef int ElementType;
typedef struct TreeNode* Position;
typedef struct TreeNode* Tree;

struct TreeNode
{
  ElementType element;
  Tree left;
  Tree right;
};

Tree makeEmpty(Tree t)
{
  if (t != NULL)
  {
    makeEmpty(t->left);
    makeEmpty(t->right);
    free(t);
  }
  return NULL;
}

Tree newTree(ElementType e)
{
  Tree tree = new TreeNode;
  tree->left = NULL;
  tree->right = NULL;
  tree->element = e;
  return tree;
}

Tree* findNode(Tree root, ElementType e)
{
  if (e < root->element)
  {
    if (root->left == NULL)
      return &root->left;
    else
      findNode(root->left, e);
  }
  else
  {
    if (root->right == NULL)
      return &root->right;
    else
      findNode(root->right, e);
  }
}

Tree buildTree(const ElementType* arr, int len)
{
  Tree root = NULL;
  for (int i = 0; i < len; ++i)
  {
    if (root == NULL)
    {
      root = newTree(arr[i]);
    }
    else
    {
      Tree* node = findNode(root, arr[i]);
      if (node != NULL)
      {
        *node = newTree(arr[i]);
      }
    }
  }
  return root;
}

void printTree(Tree root)
{
  if (root != NULL)
  {
    printTree(root->left);
    cout << root->element << ", ";
    printTree(root->right);
  }
}

bool checkBFT(Tree root)
{
  static Tree pre = NULL;
  if (root)
  {
    if (!checkBFT(root->left))
    {
      return false;
    }
    if (pre != NULL && root->element < pre->element)
    {
      //            cout << root->element << '\t';
      return false;
    }
    pre = root;
    return checkBFT(root->right);
  }

  return true;
}

Tree sampleTree()
{
  Tree root = newTree(5);
  root->left = newTree(3);
  root->left->left = newTree(2);
  root->left->right = newTree(1);
  root->right = newTree(7);
  root->right->left = newTree(8);
  root->right->right = newTree(9);
  return root;
}

int main()
{
  ElementType src[7] = { 6, 4, 8, 5, 7, 9, 3 };
  // cout << sizeof(src) << endl;
  Tree root = buildTree(src, sizeof(src) / sizeof(ElementType));
  printTree(root);
  cout << endl;
  cout << (checkBFT(root) ? "True" : "False") << endl;

  Tree sample_tree = sampleTree();
  printTree(sample_tree);
  cout << endl;
  cout << (checkBFT(sample_tree) ? "True" : "False") << endl;

  return 0;
}