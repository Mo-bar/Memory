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
  //lst.sublist(start, [end])
  //lst.shuffle();  random
  Map mp = lst.asMap(); // convert list to indexed map.
  var nbrlist = lst.whereType<int>().toList(); // only return integers
  var val = nbrlist.firstWhere((x)=> x >2); // return first value greater than 2.
  //var val = nbrlist.any((element) => false);
  //var val = nbrlist.every((element) => false);
  //var val = nbrlist.Take(2).toSet(); // return first 2 elements.
  
  
}

