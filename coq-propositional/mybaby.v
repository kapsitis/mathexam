(*
https://www.youtube.com/watch?v=U2BtteA0k8o

Everybody Loves My Baby (But My Baby Don't Love Nobody But Me)

foreach x, L(x,MyBaby) /\ foreach y (~ (y = Me) -> ~(L(MyBaby,y))


https://learning.oreilly.com/library/view/logic-as-a/9781118880005/c04.xhtml
*)

(* Set of all humans *)
Parameter HUM : Type.
Parameter Me : HUM.
Parameter MyBaby : HUM.

(* Predicate: L(x,y) is true iff "x" loves "y" *)
Parameter L : HUM*HUM -> Prop.

Check L(Me,MyBaby).


Theorem contrap : forall p q:Prop, (p->q)->(~q->~p).
Proof. 
  intros.
  intro.
  apply H0.
  apply H.
  exact H1.
Qed.




Theorem contrap2 : forall p q:Prop, (~p -> ~q) -> q -> p.
Proof. 
  intros p q.
  unfold not.




(*
  Substitute in SECOND statement y = MyBaby. 
  If MyBaby is not Me, then MyBaby does not love him. 
  
  On the other hand, ever
*)


Theorem everybody_loves: (forall x: HUM, L(x,MyBaby)) /\ 
  (forall y: HUM, ~(y=Me) -> ~(L(MyBaby,y))) -> MyBaby=Me.
Proof. 
  intros H.
  destruct H as [FIRST SECOND].
  assert (MyBaby <> Me -> ~L(MyBaby,MyBaby)).
  apply SECOND with (y := MyBaby).
  assert (L(MyBaby,MyBaby)).
  apply FIRST with (x := MyBaby).
  clear FIRST SECOND.






(*
Theorem zero_not_one : 0 <> 1.
Proof.
  unfold not.
  intros contra.
  discriminate contra.
Qed. 

Theorem False_cannot_be_proven : ~False.
Proof.
  unfold not.
  intros proof_of_False.
  contradiction.
Qed.

Theorem False_implies_nonsense : False -> 2 + 2 = 5.
Proof.
  intros contra.
  contradiction.
Qed.
*)

(*
Require Import Logic.
Require Import  ClassicalFacts.
Require Import Classical_Prop.
*)










