void main(){
  // Map accept diff datatype (list,,,)
  Map person = {
    'nom':'Mourad',
    'prenom': 'barkouch',
    'age':25
  };
  print(person);
  print(person.keys);
  print(person.values);
  print(person['nom']);
  
  person.forEach((key, value) {
    print('$key : $value');
  });
  print(person.length);
  //person.remove(key)
  
}