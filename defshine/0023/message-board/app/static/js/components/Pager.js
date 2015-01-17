var React = require("react/addons");

var Pager = React.createClass({
    getDefaultProps : function(){
        return{
            page:0,
            pages:0
        }
    },
    clickHandler: function(e){
        e.preventDefault();
        console.log(e.target.dataset.page);
        console.log(e.target.dataset.page.value);
        this.props.listMessage(e.target.dataset.page);

    },
    render : function(){
        var cx = React.addons.classSet;
        var preClass = cx({
            'previous':true,
            'disabled':this.props.page == 1
        });
        var nextClass = cx({
            'next':true,
            'disabled':this.props.page == this.props.pages
        });

        return(
            <ul className="pager">
                <li className={preClass}  onClick={this.clickHandler}>
                    <a href="#" data-page={this.props.page-1}>&larr;Prev</a>
                </li>
                <li>
                    <span>{this.props.page}/{this.props.pages}</span>
                </li>
                <li className={nextClass}  onClick={this.clickHandler}>
                    <a href="#" data-page={this.props.page+1}>Next&rarr;</a>
                </li>
            </ul>
        )
    }
});

module.exports = Pager;