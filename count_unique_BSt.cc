/*
 * 96. Given n, how many structurally unique BST that store values 1...n
 *
 * Input: 3, Output: 5
 * 
 * We solve this problem using mutual recursion
 */

#include <iostream>
using namespace std;

int countBST(int);

int uniqueHeadBST(int head, int n) {
    //recursively solving for left and right subtree
    int l_subtree_boundary = head - 1;
    int r_subtree_boundary = head + 1;
    return countBST(l_subtree_boundary - 1 + 1) * countBST(n - r_subtree_boundary + 1);
}

int countBST(int n) {
    if (n <= 1) return 1;
    int count = 0;
    for(int i = 1; i <= n; i++) {
        count += uniqueHeadBST(i, n);
    }
    return count;
}

int main() {
    int n = 4;
    int result = countBST(n);
    cout << result <<endl;
}
