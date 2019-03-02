//
// Created by linglx on 18-5-20.
//
#include <stdio.h>
#include <iostream>

#define ElementType int

using namespace std;
// std;
//------------------insert sort------------------------------
void insertion_sort(ElementType A[], int N)
{
	int pLoop, nLoop;
	ElementType temp;
	for (pLoop = 1; pLoop < N; ++pLoop) {
		temp = A[pLoop];
		for (nLoop = pLoop; nLoop > 0 && A[nLoop - 1] > temp; nLoop--) {
			A[nLoop] = A[nLoop - 1];
		}
		A[nLoop] = temp;
	}
}
//------------------shell sort------------------------------
void shell_sort(ElementType A[], int N)
{
	int i, j, increment;
	ElementType tmp;
	for (increment = N / 2; increment > 0; increment /= 2) {
		// cout<<increment<<'\t';
		/*
		//code by self
		for(i=0;i<N-increment;i++) {
			tmp = A[i];
			for(j=i;j<N-increment;j+=increment) {
				if (tmp>A[j+increment]) {
					A[j] = A[j+increment];
				}
				else
					break;
			}
			A[j] = tmp;
		}
		*/
		// code in book
		for (i = increment; i < N; i++) {
			tmp = A[i];
			for (j = i; j >= increment; j -= increment)
				if (tmp < A[j - increment]) {
					A[j] = A[j - increment];
				} else {
					break;
				}
			A[j] = tmp;
		}
	}
}
//------------------quick sort------------------------------
ElementType Median3(ElementType A[], int left, int right)
{
	int center = (left + right) / 2;
	if(A[left] > A[center]) swap(A[left], A[center]);
    if(A[left] > A[right]) swap(A[left], A[right]);
	if(A[center] > A[right]) swap(A[center], A[right]);
	cout << A[left] << '\t' << A[center] << '\t' << A[right] << endl;
	swap(A[center], A[right - 1]);
	return A[right - 1];
}
#define offset (3)
void QSort(ElementType A[], int left, int right)
{
	int i, j;
	ElementType pivot;

	if(left + offset <= right)
	{
		pivot = Median3(A, left, right);
		i = left;
		j = right - 1;
		for (;;)
		{
			while (A[++i] < pivot){}
			while (A[--j] > pivot){}
			if(i < j)
				swap(A[i], A[j]);
			else
				break;
		}
		swap(A[i], A[right - 1]);

		QSort(A, left, i - 1);
		QSort(A, i + 1, right);
	} else
	{
		insertion_sort(A + left, right - left + 1);
	}
}
void QuickSort(ElementType A[], int N)
{
	QSort(A, 0, N - 1);	QSort(A, 0, N - 1);
}
//-----------------------------------------------
int main(int argc, char const *argv[])
{
	int data[] = {9, 1, 3, 2, 11, 33, 55, 3, 7, 7, 23, 5, 11, 6, 4};
	int N = sizeof(data) / sizeof(int);

	// insertion_sort(data, N);
	// shell_sort(data, N);
	QuickSort(data, N);
	for (int i = 0; i < N; ++i)
  {
		cout << data[i] << " ";
	}
	return 0;
}
