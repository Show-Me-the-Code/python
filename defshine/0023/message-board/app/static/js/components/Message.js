var React = require("react");

var Message = React.createClass({
    render : function(){
        var msg = this.props.message;
        return(
            <div>
                <h3>{msg.author}&nbsp;&nbsp;
                    <small>{msg.time.toLocaleString()}</small>
                </h3>
                <p>{msg.content}</p>
            </div>
        )
    }
});

module.exports = Message;