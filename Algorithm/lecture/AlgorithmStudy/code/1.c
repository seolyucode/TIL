// 큐 구현하기 (Queue)

// Q.create(y)
// Q.push(y)
// Q.pop()
// Q.front()
// Q.size()

#include <stdio.h>

struct Queue {
  
  int data[10];
  int f, r;
  int capacity;
  
  void create(int y) {
    capacity = y;
    f = 0;
    r = 0;
  }
  
  void push(int y) {
    if(r - f >= capacity) {
      printf("Queue overflow!\n");
    }
    else {
      data[r++] = y;
    }
  }
  
  void pop() {
    if(r - f <= 0) {
      printf("Queue underflow!\n");
    }
    else {
      data[f] = 0;
      f++;
    }
  }
  
  int front() {
    // 큐의 맨 앞에 있는 원소를 반환.
    // 단, 반환할 것이 없다면 -1을 반환.
    
    if(r - f <= 0) {
      return -1;
    }
    else {
      return data[f];
    }
  }
  
  int size() {
    return r - f;
  }
};

int main() {
  Queue q1;
  
  q1.create(4);
  
  for(int i=0; i<20; i++) {
    q1.push(i);
    q1.push(i+1);
    q1.push(i+2);
    q1.push(i+3);
    
    q1.pop();
    q1.pop();
    q1.pop();
    q1.pop();
  }
  
  q1.push(1);
  q1.push(2);
  
  printf("%d\n", q1.front());  // 1
  
  q1.pop();
  
  printf("%d\n", q1.front());  // 2
  
  q1.pop();

  return 0;
}