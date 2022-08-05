// -- Set --
// ---------
// {1} Set Items Are Enclosed between Curly Braces
// {2} Set Items Are Not Ordered And Not Indexed
// {3} Set Indexing and Slicing Cant Be Done
// {4} Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
// {5} Set Items Is Unique
void main(){
  Set nbr = {1,23,4,5,55};
  nbr.addAll([0,3]);
  print(nbr);
  print(nbr.toList()); // convert set list
  print([23,44,5].toSet()); // convert list to set.
}