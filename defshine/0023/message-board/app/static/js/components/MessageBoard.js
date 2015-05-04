var React = require("react");
var MessageList = require("./MessageList");
var MessageForm = require("./MessageForm");
var Pager =  require("./Pager");

var MessageBoard = React.createClass({
    getInitialState : function(){
        return {
            messages: [],
            page:0,
            pages:0
        }
    },
    submitMessage : function (author, content) {
        $.ajax({
            type:'post',
            url:'/message',
            data:{author:author,content:content}
        }).done(function (data) {
            console.log(data);
            this.listMessage(1);
        }.bind(this));
    },
    listMessage : function(page){
        console.log("listMessages page:"+page)
        $.ajax({
            type:'get',
            url:'/messages',
            data:{page:page}
        }).done(function (resp) {
            if(resp.status == "success"){
                var pager = resp.pager;
                console.log(pager);
                this.setState({
                    messages:pager.messages,
                    page:pager.page,
                    pages:pager.pages
                });
            }
        }.bind(this));
    },
    componentDidMount : function(){
        this.listMessage(1);
    },
    render : function(){
        var pager_props = {
            page : this.state.page,
            pages : this.state.pages,
            listMessage : this.listMessage
        };
        return(
            <div>
                <MessageForm submitMessage={this.submitMessage}/>
                <MessageList messages = {this.state.messages}/>
                <Pager {...pager_props}/>
            </div>
        )
    }
});

module.exports = MessageBoard;
