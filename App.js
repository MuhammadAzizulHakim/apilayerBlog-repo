import React, {Component} from 'react';
import Newss from './components/newss';
	
class App extends Component {
	render() {
	    return (
            <Newss newss={this.state.newss} />
        )
	}
	
	state = {
        newss: []
    };

    componentDidMount() {
        fetch("http://api.mediastack.com/v1/news?access_key=YOUR_ACCESS_KEY&languages=en")
            .then(res => res.json())
            .then((res) => {
                this.setState({ newss: res.data })
            })
            .catch(console.log)
    }
}

export default App;