/*Recover a secret string from random triplets
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string. 
A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".
As a simplification, you may assume that no letter occurs more than once in the secret string.
You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
-------------------------
CODE#*/
import java.util.*;
public class SecretDetective {
  public String recoverSecret(final char[][] triplets) {
    final Set<Character> characters = new HashSet<>();
    final Map<Character, Set<Character>> partialOrder = new HashMap<>();
    for (final char[] triplet : triplets) {
      for (int i = 0; i < triplet.length; i++) {
        final char c = triplet[i];
        characters.add(c);
        Set<Character> after = partialOrder.get(c);
        if (after == null) {
          after = new HashSet<>();
          partialOrder.put(c, after);
        }
        for (int j = i + 1; j < triplet.length; j++) {
          after.add(triplet[j]);
        }
      }
    }
    transitiveClosure(partialOrder);
    final int length = characters.size();
    final char[] secret = new char[length];
    for (final Map.Entry<Character, Set<Character>> entry : partialOrder.entrySet()) {
      secret[length - entry.getValue().size() - 1] = entry.getKey();
    }
    return String.valueOf(secret);
  }
  private <E> void transitiveClosure(final Map<E, Set<E>> partialOrder) {
    boolean changed = false;
    for (final Set<E> oldValues : partialOrder.values()) {
      final Set<E> newValues = new HashSet<>();
      for (final E oldValue : oldValues) {
        newValues.addAll(partialOrder.get(oldValue));
      }
      changed |= oldValues.addAll(newValues);
    }
    if (changed) {
      transitiveClosure(partialOrder);
    }
  }
}
