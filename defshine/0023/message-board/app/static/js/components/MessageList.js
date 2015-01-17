var React = require("react");
var Message = require("./Message");

var MessageList = React.createClass({
    render : function () {
        var messages = this.props.messages.map(function(item){
            return <Message message={item}/>
        });
        console.log(messages);
        return(
            <div>
                {messages}
            </div>
        )
    }
});

module.exports = MessageList;