from pyteal import *


def approval_program():
    
    
    on_creation = Seq(
        [
            App.globalPut(Bytes("Creator"), Txn.sender()),
            Assert(Txn.application_args.length() == Int(4)),
            App.globalPut(Bytes("member1"), Btoi(Txn.application_args[0])),
            App.globalPut(Bytes("member2"), Btoi(Txn.application_args[1])),
            App.globalPut(Bytes("member3"), Btoi(Txn.application_args[2])),
            App.globalPut(Bytes("member4"), Btoi(Txn.application_args[3])),
            Return(Int(1)),
        ]
    )

    on_page_change = Return(
        Or(Txn.sender == App.globalGet(Bytes("member1")),
            Txn.sender == App.globalGet(Bytes("member2")),
            Txn.sender == App.globalGet(Bytes("member3")),
            Txn.sender == App.globalGet(Bytes("member4")),
         ),
    )
    is_creator = Txn.sender() == App.globalGet(Bytes("Creator"))
    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.DeleteApplication, Return(is_creator)],
        [Txn.on_completion() == OnComplete.UpdateApplication, Return(is_creator)],
        [Txn.on_completion() == OnComplete.CloseOut, Return(Int(1))],
        [Txn.on_completion() == OnComplete.OptIn, on_page_change],
    )

    return program


def clear_state_program():
    get_vote_of_sender = App.localGetEx(Int(0), App.id(), Bytes("voted"))
    program = Seq(
        [
        Return(Int(1)),
        ]
    )

    return program


if __name__ == "__main__":
    with open("vote_approval.teal", "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)

    with open("vote_clear_state.teal", "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)
