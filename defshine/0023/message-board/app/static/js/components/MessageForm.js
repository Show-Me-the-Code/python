var React = require("react");

var MessageForm = React.createClass({
    handleSubmit : function (e) {
        e.preventDefault();
        var author = this.refs.author.getDOMNode().value.trim();
        var content = this.refs.content.getDOMNode().value.trim();

        this.props.submitMessage(author,content);

        this.refs.author.getDOMNode().value = "";
        this.refs.content.getDOMNode().value = ""
    },
    render : function(){
        return(
              <div className="well">
                    <h4>Leave a Message:</h4>
                    <div role="form">
                        <div className="form-group">
                            <input ref="author" className="form-control" placeholder="Name"/>
                            <textarea ref="content" className="form-control" rows="3" placeholder="Leave your message here"></textarea>
                        </div>
                        <a  className="btn btn-primary" onClick={this.handleSubmit}>Submit</a>
                    </div>
                </div>
        )
    }
});

module.exports = MessageForm;