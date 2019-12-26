(* 
https://stackoverflow.com/questions/23996056/elim-a-double-negation-hypothesis-in-coq-proof-assistant
https://github.com/coq/coq/wiki/CoqAndAxioms
https://github.com/coq/coq/wiki/The-Logic-of-Coq
https://github.com/coq/coq/blob/master/theories/Logic/Classical_Prop.v
https://stackoverflow.com/questions/14644086/proving-p-q-q-p-using-coq-proof-assistant
http://flint.cs.yale.edu/cs428/coq/sf/Logic.html
*)

(*
NOTE. This proof is not intuitionistic.
It uses this axiom from Classical_Prop.v:
Axiom classic : forall (P : Prop), P \/ ~ P.
The 1st part of this proof repeats the proof of NNPP (Classical_Prop.v).
The 2nd part of this proof just unfolds "not" statements.
*)
(* EXERCISE 1.3.2 SOLUTION *)
Example ex_1_3_2: forall p:Prop, ~(~p) <-> p.
Require Import Classical_Prop.
Proof.
  split.
(* 1nd part: ~~p -> p *)
  unfold not.
  intros.
  elim (classic p).
  auto. 
  intro NP.
  elim (H NP).
(* 2nd part: p -> ~~ p *)
  intros H.
  unfold not. 
  intros G.
  apply G.
  exact H.
Qed. 






