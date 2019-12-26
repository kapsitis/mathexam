Lemma id_p : forall p: Prop, p -> p.
Proof.
  intros p H.
  exact H.
Qed.

Lemma imp_trans : forall p q r: Prop, (p->q)->(q->r)->p->r.
Proof.
  intros p q r.
  intros H1.
  intros H2.
  intros H3.
  apply H2.
  apply H1.
  exact H3.
Qed.


(*
https://coq.inria.fr/tutorial/1-basic-predicate-calculus
*)

Lemma or_commutative : forall a b: Prop, a \/ b -> b \/ a.
Proof. 
  intros A B H.
  elim H.
  intro HA.
  clear H.
  right.
  exact HA.
  intro HB.
  left.
  exact HB.
Qed.

Lemma or_commutative1 : forall a b: Prop, a \/ b -> b \/ a.
Proof. 
  intros a b H.
  destruct H as [HA | HB].
  right.
  exact HA.
  left.
  exact HB.
Qed.

