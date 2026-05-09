/** Pair class to store key-value pairs */
// class Pair {
//   /**
//    * @param {number} key The key to be stored in the pair
//    * @param {string} value The value to be stored in the pair
//    */
//   constructor(key, value) {
//       this.key = key;
//       this.value = value;
//   }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[]}
     */
    mergeSort(pairs) {
        return this.mergeSortHelper(pairs, 0, pairs.length - 1)
        }
    
    mergeSortHelper(pairs, s, e){
        if ( (e - s + 1) <= 1) {
            return pairs;
        }
        let m = Math.floor((s + e) / 2);

        this.mergeSortHelper(pairs, s, m);
        this.mergeSortHelper(pairs, m + 1, e);

        this.merge(pairs, s, m, e);

        return pairs;
    }
    
    merge(arr, s, m, e) {
        let L = arr.slice(s, m +1);
        let R = arr.slice(m + 1, e + 1);
        let i=0,  j =0, k = s;
        while ( (i < L.length )  &&  ( j < R.length) ){
            if (L[i].key <= R[j].key){
                arr[k] = L[i];
                k++;
                i++; 
            } else {
                arr[k] = R[j];
                k++;
                j++;
            }
        }
        while (i < L.length ) {
            arr[k] = L[i];
            k++;
            i++; 
        }
        while (j < R.length ) {
            arr[k] = R[j];
            k++;
            j++; 
        }
    }
}
