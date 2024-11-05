/*

#include <vector>
using namespace std;

// Time: O(n) | Space: O(1)
vector<int> moveElementToEnd(vector<int> array, int toMove) {
  int left = 0;
  int right = array.size() - 1;

  while(left < right){
    if(array[right] == toMove){
      right--;
    }
    else{
      swap(array[left], array[right]);
      left++;
    }
  }
  return array;
}


*/