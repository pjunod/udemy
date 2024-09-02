import unittest
import qsort

class TestQickSortMethods(unittest.TestCase):

    def test_swap(self):
        unswapped_list = [5, 1, 9, 4, 6, 2]
        swapped_list = [2, 1, 9, 4, 6, 5]
        qsort.swap(unswapped_list, 0, 5)

        self.assertListEqual(unswapped_list, swapped_list)

    def test_pivot(self):
        plist = [5, 4, 6, 1, 3, 2]
        reslist = [2, 4, 1, 3, 5, 6]
        p_index = 4

        ret_index = qsort.pivot(plist, 0, 5)

        self.assertEqual(ret_index, p_index)

        self.assertListEqual(reslist, plist)

    def test_quicksort(self):
        reslist = [1,2,3,4,5,6,7]
        testlist = qsort.quick_sort([4,6,1,7,3,2,5])
        self.assertListEqual(testlist, reslist)


if __name__ == "__main__":
    unittest.main(verbosity=2)
