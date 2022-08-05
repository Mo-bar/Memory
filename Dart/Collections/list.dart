void main(){
// List props.
// [1] list items are eclosed between square brackets.
// [2] list accept different datatype.
// [3] List Are Mutable => Add, Delete, Edit
// [4] List Items Is Not Unique
  List lst = ['ah',23,22.2,'hhhh',false,[23,33,45,['a','b']]];
  print(lst.last[3][1]);
  print(lst.first);
  print(lst.isNotEmpty);
  print(lst.isEmpty);
  print(lst.reversed);
  //print(lst.single);
  lst.addAll([1,1]); // added at last index
  lst.insert(0, [0,0]); // added at index
  print(lst);
  //lst.replaceRange(start, end, replacements)
  lst.remove('ah');
  lst.removeAt(2);
  //lst.removeRange(start, end)
  
  
}

