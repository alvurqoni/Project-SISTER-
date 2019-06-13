from mpi4py import MPI
import numpy as np
import pandas as pd
import time as tm
import xlrd

start = tm.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = xlrd.open_workbook('data.xlsx')
test = data.sheet_by_index(0)
temp1 = []
temp2 = []
temp3 = []
temp4 = []

def quickSort(alist):

  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):

  if first<last:
      splitpoint = partition(alist,first,last)
      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):

  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
          leftmark = leftmark + 1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1

      if rightmark < leftmark:
          done = True
      else:
          temp = alist[leftmark]
          alist[leftmark] = alist[rightmark]
          alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark

if rank == 1:
    for i in range (1,2500):
        temp1.append(test.cell_value(i,0))
    quickSort(temp1)
    print("rank ke: ",rank) 
    print("hasil dari sorting : ",temp1)
elif rank == 2:
    for i in range (2501,5000):
        temp2.append(test.cell_value(i,0))
    quickSort(temp2)
    print("rank ke: ",rank)
    print("hasil dari sorting : ",temp2)
elif rank == 3:
    for i in range (5001,7500):
        temp3.append(test.cell_value(i,0))
    quickSort(temp3)
    print("rank ke: ", rank)
    print("hasil dari sorting : ",temp3)
elif rank == 0:
    for i in range (7501,10000):
        temp4.append(test.cell_value(i,0))
    quickSort(temp4)
    print("rank ke: ", rank)
    print("hasil dari sorting : ", temp4)

end = tm.time()
waktu = end - start

print('waktu eksekusi : ', waktu)





